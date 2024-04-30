module.exports = {
  apps: [{
    name: 'greetings-app-dev',
    script: 'app.py',
    env: {
      PORT: process.env.PORT,  // Get port from environment variable
    },
  }],
};
