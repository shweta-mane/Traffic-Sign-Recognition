import React, { Component } from "react";
import axios from "axios";

class UploadPic extends Component {
  state = {
    selectedFile: "",
    image_class: "",
    uploadedFiles: [],
    currentImage: "",
    prob:""
  };

  onPicSubmit = (e) => {
    e.preventDefault();


    console.log(this.state.selectedFile);


    console.log(this.state.uploadedFiles);
   
    for (let i=0;i<this.state.uploadedFiles.length;i++){
      
        //(function (eachFile) {
          setTimeout(() => {
            const data = new FormData();
            data.append("image", this.state.uploadedFiles[i]);
            let payload = {
              data
            };

            try {
              axios

                // .//post(`http://54.177.173.161/trafficsignrecapi/predict`, data)

                .post(`http://127.0.0.1:5000/trafficsignrecapi/predict`, data)
                .then((res) => {
                  console.log(res);
                  console.log(res.data.image_class);
                  this.setState({ 
                    image_class: res.data.image_class, 
                    prob: res.data.prob
                  
                  });
                  this.setState({ currentImage: URL.createObjectURL(this.state.uploadedFiles[i]) })
                })
                .catch((err) => {
                  console.log(err);
                });
              //this.setState({currentImage : URL.createObjectURL(eachFile)})

            } catch (error) {
            }
          },i* 3000);
        //})(eachFile);
    }
  };
  render() {
    return (
      <div className="container" align="center">
        <div className="card p-3 m-3">
          <div className="card-title">UploadPic</div>
          <div className="card-body">
            <label style={{ fontSize: "15px", fontWeight: "500" }} for="img">
              Your Picture:
              <img src={this.state.currentImage} />
            </label>
            <form onSubmit={this.onPicSubmit} enctype="multipart/form-data">
              <input
                style={{ fontSize: "13px" }}
                type="file"
                name="file"
                id="file"
                multiple
                onChange={(event) => {
                  console.log(event.target.files[0]);
                  console.log('files', event.target.files.length);
                  this.setState({
                    selectedFile: event.target.files[0],
                    uploadedFiles: event.target.files
                  });
                }}
              />
              <input className='btn btn-success' type='submit' value='upload pic'></input>
            </form>
          </div>
        </div>

        {this.state.image_class}
        {this.state.prob}

      </div>

    );
  }
}
export default UploadPic;
