import React,{ useState } from 'react';
import { Modal, Input, Button } from 'semantic-ui-react';

function CreatePlaylist(props) {
    const[playListName, setName] = useState("")
    return (
        <Modal
        size={'mini'}
        open={props.createPlaylist}
        onClose={() => props.showCreatePlaylist(false)}
      >
        <Modal.Header>Create Your Playlist</Modal.Header>
        <Modal.Content>
            <p>Name :</p>
            <Input 
                size="large"
                placeholder='Enter playList Name' 
                value={playListName}
                onChange={(e)=>setName(e.target.value)}
            />
        </Modal.Content>
        <Modal.Actions>
          <Button negative onClick={() => props.showCreatePlaylist(false)}>
            No
          </Button>
          <Button positive onClick={() => props.addPlayList(playListName)}>
            Yes
          </Button>
        </Modal.Actions>
      </Modal>
    )
}

export default CreatePlaylist
