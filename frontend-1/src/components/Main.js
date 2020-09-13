import React, { Component } from "react";
import { Route } from "react-router-dom";
import  UploadPic from "./UploadPic"
import  Dashboard from "./Dashboard"

class Main extends Component {
  render() {
    return (
   <div>

        {/*<Route path="/uploadPic" component={UploadPic} />*/}
        <Route path="/" component={Dashboard} />
        
      
      </div>
    );
  }
}
//Export The Main Component
export default Main;
