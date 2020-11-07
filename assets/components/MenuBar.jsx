import React, {useState} from 'react';
import { Menu, Input } from 'semantic-ui-react';

function MenuBar(props) {
  const [songname, setSong] = useState("")

    function search(e){
      if (e.key === "Enter") {
        props.searchSongs(songname);
        setSong("");
      }
    }
    return (
        <Menu attached="top" tabular>
          <Menu.Item
            name='home'
            active={props.activeMenu === 'home'}
            onClick={()=>props.handleMenu('home')}
          />
          <Menu.Item
            name='PlayList'
            active={props.activeMenu === 'playList'}
            onClick={()=>props.handleMenu('playList')}
          />
          <Menu.Menu position='right'>
            <Menu.Item>
              <Input
                transparent
                icon={{ name: 'search', link: true }}
                placeholder='Search Songs...'
                onChange={(e)=>setSong(e.target.value)}
                onKeyPress={(e)=>search(e)}
                value={songname}
              />
            </Menu.Item>
          </Menu.Menu>
        </Menu>
    )
}

export default MenuBar;
