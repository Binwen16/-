const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // devServer: {
  //   proxy: {
  //     '^/api': {
  //       target: 'http://127.0.0.1:8000',
  //       changeOrigin: true, // 允许跨域
  //       pathRewriter: {
  //         '^/api': '',
  //       },
  //     },
  //   },
  // },
})