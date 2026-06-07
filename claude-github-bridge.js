const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
if (!GITHUB_TOKEN) {
  console.error('Missing GITHUB_TOKEN environment variable');
  process.exit(1);
}

const githubApi = axios.create({
  baseURL: 'https://api.github.com',
  headers: {
    Authorization: `token ${GITHUB_TOKEN}`,
    Accept: 'application/vnd.github+json',
    'User-Agent': 'claude-github-bridge'
  }
});

async function getFileSha(owner, repo, path, branch) {
  try {
    const resp = await githubApi.get(`/repos/${owner}/${repo}/contents/${encodeURIComponent(path)}`, {
      params: { ref: branch }
    });
    return resp.data.sha;
  } catch (err) {
    if (err.response && err.response.status === 404) return null;
    throw err;
  }
}

app.post('/apply-change', async (req, res) => {
  const { owner, repo, path, content, message, branch = 'main' } = req.body;
  if (!owner || !repo || !path || !content || !message) {
    return res.status(400).json({ error: 'owner, repo, path, content, and message are required' });
  }

  try {
    const sha = await getFileSha(owner, repo, path, branch);
    const encoded = Buffer.from(content, 'utf8').toString('base64');

    const payload = {
      message,
      content: encoded,
      branch
    };
    if (sha) payload.sha = sha;

    const response = await githubApi.put(`/repos/${owner}/${repo}/contents/${encodeURIComponent(path)}`, payload);
    res.json({
      status: 'ok',
      action: sha ? 'updated' : 'created',
      path,
      sha: response.data.content.sha,
      url: response.data.content.html_url
    });
  } catch (err) {
    const status = err.response ? err.response.status : 500;
    const errorText = err.response ? err.response.data : err.message;
    res.status(status).json({ error: errorText });
  }
});

app.listen(3000, () => {
  console.log('Claude GitHub bridge running on port 3000');
});
