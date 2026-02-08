import React from 'react';

const HumanParticles = () => {
    return (
        <div style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            zIndex: 1,
            pointerEvents: 'none',
            background: 'linear-gradient(135deg, #E7DDDD 0%, #d1c4c4 100%)'
        }}>
            {/* Placeholder for particles */}
        </div>
    );
};

export default HumanParticles;
