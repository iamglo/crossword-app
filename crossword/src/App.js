import React, {Component} from 'react';
import '@fortawesome/fontawesome-free/css/all.min.css';
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";
import AnswerTable from './components/AnswerTable'
import Header from './components/Header'
import About from './components/About'
import NotFound from './components/NotFound'
import SearchBar from './components/SearchBar'

import clueService from './services/clues'
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

class App extends Component {
  constructor(props){
    super(props);
    this.changeState = this.changeState.bind(this);
    this.state = {data : []}
  }

  changeState (res) {
    this.setState({data: res});
  }

  async componentDidMount() {
    clueService.getAll()
    .then((res) => {
      this.setState({data: res})
    })
    .catch(console.log)
  }

  render() {
    return (
      <div className="App">
          <Header></Header>
          <br></br>
          <Switch>
            <Route exactly path="/about">
              <About></About>
            </Route>
            <Route exactly path="/stats">
            </Route>
            <Route exactly path="/home">
              <h1> Search </h1>
              <SearchBar changeState={this.changeState}></SearchBar>
              <AnswerTable data={this.state.data.slice(0,50)}></AnswerTable>
            </Route>
            <Route>
              <NotFound />
            </Route>
          </Switch>
      </div>
    );
  }
}

export default App;
