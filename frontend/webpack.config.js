const path = require("path");
const webpack = require("webpack");
module.exports = {
  entry: "./src/index.js",
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  performance: {
    hints: false,
    maxEntrypointSize: 512000,
    maxAssetSize: 512000
},
  output: {
    path: path.resolve(__dirname, "./backend/static/frontend/"),
    filename: "[name].js",
  },
  module: {
    rules: [
      
      {
        test: /\.js|.jsx$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
      {
        test: /\.less$/i,
        use: [
          // compiles Less to CSS
          "style-loader",
          "css-loader",
          "less-loader",
        ],
      },
      {
        test: /\.(sa|sc|c)ss$/,
        use: ["style-loader", "css-loader", "sass-loader"]
      },
      {
          test: /\.(jpe?g|png|gif|svg|json)$/i, 
          loader: 'file-loader',
          options: {
            name: '/images/[name].[ext]'
          }
      }
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
