import React from 'react';
import { Pagination } from 'semantic-ui-react';

function Paginations() {
    return (
        <div className="cursors">
            <Pagination
            defaultActivePage={1}
            firstItem={null}
            lastItem={null}
            secondary
            totalPages={3}
        />
    </div>
    )
}

export default Paginations
