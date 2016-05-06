import React, { Component } from 'react';
import ReactSwipe from 'react-swipe';

import ShotCard from './ShotCard';


export default class ShotContainer extends Component {
  next() {
    this.refs.reactSwipe.next();
  }

  prev() {
    this.refs.reactSwipe.prev();
  }

  render() {
    const shots = [...Array(12).keys()]
                  .map(i => <ShotCard key={i} shotNumber={i + 1} />);

    return (
      <div>
        <ReactSwipe ref="reactSwipe" className="carousel" swipeOptions={{ continuous: false }}>
            {[...shots]}
        </ReactSwipe>

        <div>
          <button type="button" onClick={() => this.refs.reactSwipe.prev()}>&lt; prev</button>
          <button type="button" onClick={() => this.refs.reactSwipe.next()}>next &gt;</button>
        </div>
      </div>
    );
  }
}
