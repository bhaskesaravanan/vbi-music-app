import React from 'react';
import { Pagination } from 'semantic-ui-react';

function Paginations() {
    function d(e) {
        console.log(e)
    }
    return (
        <div className="cursors">
            <Pagination
            defaultActivePage={1}
            firstItem={null}
            lastItem={null}
            secondary
            totalPages={3}
            onClick={(e)=> d(e)}
        />
    </div>
    )
}

export default Paginations
