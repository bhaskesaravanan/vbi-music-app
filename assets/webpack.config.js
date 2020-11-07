const path = require("path");

module.exports = {
  entry: [path.join(__dirname, "./index.js")],
  output: {
    path: path.join(__dirname, "../static/js/dist"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
    ],
  },
  // devServer: {
  //   contentBase: path.join(__dirname, "dist"),
  //   compress: true,
  //   port: 8000,
  // },
};
