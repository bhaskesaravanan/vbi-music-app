import React from 'react';
import {Modal} from 'semantic-ui-react';

function PlayListModel(props) {
    return (
        <Modal
        className="play-list-modal"
        size={"mini"}
        open={props.showPlayListModel}
        onClose={() => props.showPlayListModal(false)}
      >
        <Modal.Header>PlayList</Modal.Header>
        <Modal.Content scrolling={true}>
        <Modal.Description>
            {   props.playLists.map((list)=>
                <span key={list.id} className="play-list-name" onClick={()=>props.addSongsToPlaylist(props.songId, list.id )}>
                    {list.name}
                </span>
            )}
            </ Modal.Description>
        </Modal.Content >
      </Modal>
    )
}

export default PlayListModel
