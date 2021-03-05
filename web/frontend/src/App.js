import React, { Component } from 'react';
import axios from 'axios';
import Menu from './menu';
import BlogList from './blog/BlogList';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentWillMount() {
    axios.get('http://localhost:8000/yonghun/blog/api/list/').then(res => {
      this.setState({ items: res.data });
    });
  }

  render() {
    return (
      <div>
        <Menu/>
        <BlogList/>
        <ul>
          {this.state.items.map(item =>
            <li key={item.title}><a href={item.id}>{item.title}</a></li>
          )}
        </ul>
      </div>

    );
  }
}

export default App;