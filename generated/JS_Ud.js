const express = require('express');
const app = express();
const axios = require('axios');
const fs = require('fs');
const ytdl = require('ytdl-core');
const url = require('url');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/download', (req, res) => {
  const videoUrl = req.body.url;
  const video = ytdl(videoUrl, {
    filter: 'audioandvideo',
  });

  video.pipe(fs.createWriteStream('download.mp4'));

  video.on('info', (info) => {
    res.json({
      title: info.title,
      length: info.length,
    });
  });

  video.on('end', () => {
    res.download('download.mp4', 'video.mp4', () => {
      fs.unlinkSync('download.mp4');
    });
  });

  video.on('error', (err) => {
    console.log(err);
    res.status(500).json({ message: 'Failed to download video' });
  });
});

app.get('/download', (req, res) => {
  const videoUrl = req.query.url;
  const video = ytdl(videoUrl, {
    filter: 'audioandvideo',
  });

  res.header('Content-Disposition', `attachment; filename="video.mp4"`);
  res.header('Content-Type', 'video/mp4');

  video.pipe(res);
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
