const express = require('express');
const rateLimit = require('./rateLimiter');
const httpProxy = require('http-proxy');

const app = express();
const proxy = httpProxy.createProxyServer();
const target = 'http://localhost:3000';

app.use(rateLimit);

app.use((req, res) => {
  proxy.web(req, res, { target });
});

app.listen(8080, () => console.log('Claire proxy listening on 8080'));
