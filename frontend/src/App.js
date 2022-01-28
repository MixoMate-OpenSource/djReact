import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App({ ...props }) {
    const data = `function onLoad(editor) {
  console.log("I've loaded!");
  }`;

    return (

        <Router>
            <h1 id="h1">Frontend: ReactJs</h1>
            <h1 id="h1">Backend: Django</h1>
            <h4>Setup By: rockvns</h4>
        </Router>


    );
}

export default App;