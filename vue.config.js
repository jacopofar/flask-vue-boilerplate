module.exports = {
  lintOnSave: false,
  devServer: {
    port: 8090,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        secure: false,
      },
      '/login': {
        target: 'http://localhost:8080',
        secure: false,
      },
    },
  },
};
