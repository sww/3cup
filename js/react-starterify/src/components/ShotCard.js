import React from 'react';

const ShotCard = ({ shotNumber }) => (
  <div>
    SHOT # {shotNumber}
  </div>
);

ShotCard.propTypes = { shotNumber: React.PropTypes.number };

export default ShotCard;
