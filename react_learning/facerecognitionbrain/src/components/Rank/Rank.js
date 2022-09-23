import React from 'react';


const Rank = ({ name, entries }) => {
    return (
        <div>
        <div className='white f3'>
           { /* We just make the two props dynamic so that 
            they can have the current values based on the user name
            and behviour */}
            {`${name}, your current entry count is...`}
            
        </div>
        <div className='white f1'>
            {entries}
        </div>
        </div>
    );
}

export default Rank;