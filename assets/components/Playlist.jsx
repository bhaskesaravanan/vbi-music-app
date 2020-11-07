import React from 'react';
import { Segment, Card, Button, Icon } from 'semantic-ui-react';

function Playlist(props) {
    return (
        <Segment className="music-segment" attached="bottom" loading={props.songloader}>
            <div className ="playlist-btn">
            <Button 
                animated 
                floated="right" 
                className="add-playlist" 
                color="blue"
                onClick={()=>props.showCreatePlaylist(true)}
            >
                <Button.Content visible>Create Playlist</Button.Content>
                <Button.Content hidden>
                    <Icon name='add' />
                </Button.Content>
            </Button>
            </div>
        <Card.Group>
            {
              props.playLists.map((playList, index)=>{
                  return(
                    <Card key={index} className="playlist-card">
                        <Card.Content onClick={()=>props.showPlayListSong(playList.id, true)}>
                            <Card.Header content={playList.name} />
                            <Card.Meta content={playList.created_date} />
                        </Card.Content>
                        <Card.Content extra onClick={()=>props.deletePlayList(playList.id)}>
                            <Icon name="remove" />
                        Delete
                        </Card.Content>
                    </Card>
                  )
              })  
            }
        </Card.Group>
        </Segment>
  )
}

export default Playlist
