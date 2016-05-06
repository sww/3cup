import React from 'react';
import { render } from 'react-dom';
import { Router, Route, hashHistory } from 'react-router';
import App from './components/App';
import PoweredBy from './components/Powered-by';
import About from './components/About';
import ShotContainer from './components/ShotContainer';
import ShotCard from './components/ShotCard';

window.React = React;

render(
  (<Router history={hashHistory}>
    <Route path="/" component={App}>
      <Route path="/about" component={About} />
      <Route path="/poweredby" component={PoweredBy} />
      <Route path="/shotcontainer" component={ShotContainer} />
      <Route path="/shotcard" component={ShotCard} />
    </Route>
  </Router>), document.getElementById('content')
);
