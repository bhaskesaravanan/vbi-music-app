import React from 'react';
import {Header, Icon} from 'semantic-ui-react';

function Headers() {
    return (
        <div className="music-header">
            <Header as='h2'>
                <Icon name='magic' />
                <Header.Content>VBI Music</Header.Content>
            </Header>
        </div>
    )
}

export default Headers
