import React, { Component, Fragment } from 'react';
import './App.css';
import Main from './components/Main';
import {BrowserRouter} from 'react-router-dom';
//Comment


//App Component
class App extends Component {
  render() {
    return (
      <Fragment>
      
      <BrowserRouter>
      
        <div>
          {}
          <Main/>
        </div>
      </BrowserRouter>
      </Fragment>

    );
  }
}

export default App;
