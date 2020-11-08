export async function fetchSongs(playlist_id=null) {
    let url = `/api/songs`;
    if(playlist_id)
        url = `${url}?playlist_id=${playlist_id}`
    try {
      const reqObj = {
        headers: {
          "Content-Type": "application/json",
        }
      };
      const result = await fetch(url, reqObj);
      const response = await result.json();
      return response;
    } catch (err) {
      console.log(err);
    }
    return null;
}


export async function addSongsToPlayList(payload) {
const url = `/api/playlists/song`;
try {
    const reqObj = {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "x-api-key": payload.user_id,
    },
    body: JSON.stringify(payload),
    };
    const result = await fetch(url, reqObj);
    const response = await result.json();
    return response;
} catch (err) {
    console.log(err);
}
return null;
}

export async function deleteSongsFromPlayList(payload) {
    const url = `/api/playlists/song`;
    try {
        const reqObj = {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": payload.user_id,
        },
        body: JSON.stringify(payload),
        };
        const result = await fetch(url, reqObj);
        const response = await result.json();
        return response;
    } catch (err) {
        console.log(err);
    }
    return null;
}

export async function savePlayList(payload) {
    const url = `/api/playlists`;
    try {
        const reqObj = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": payload.user_id,
        },
        body: JSON.stringify(payload),
        };
        const result = await fetch(url, reqObj);
        const response = await result.json();
        return response;
    } catch (err) {
        console.log(err);
    }
    return null;
}

export async function fetchPlayList(user_id=null) {
    let url = `/api/playlists`;
    if(user_id)
        url = `${url}?user_id=${user_id}`
    try {
        const reqObj = {
        headers: {
            "Content-Type": "application/json",
            "x-api-key": user_id,
        },
        };
        const result = await fetch(url, reqObj);
        const response = await result.json();
        return response;
    } catch (err) {
        console.log(err);
    }
    return null;
}


export async function deletePlayList(payload) {
    const url = `/api/playlists`;
    try {
        const reqObj = {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": payload.user_id,
        },
        body: JSON.stringify(payload),
        };
        const result = await fetch(url, reqObj);
        const response = await result.json();
        return response;
    } catch (err) {
        console.log(err);
    }
    return null;
}

export async function signup(payload) {
    const url = `/signup`;
    try {
        const reqObj = {
        method: "post",
        headers: {
            "Content-Type": "application/json",
            // Authorization: `Bearer ${clientToken}`,
        },
        body: JSON.stringify(payload),
        };
        const result = await fetch(url, reqObj);
        const response = await result.json();
        return response;
    } catch (err) {
        console.log(err);
    }
    return null;
}

export async function login(payload) {
    const url = `/login`;
    try {
        const reqObj = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            // Authorization: `Bearer ${clientToken}`,
        },
        body: JSON.stringify(payload),
        };
        const result = await fetch(url, reqObj);
        const response = await result.json();
        return response;
    } catch (err) {
        console.log(err);
    }
    return null;
}

export async function logout(payload) {
    const url = `/logout`;
    try {
        const reqObj = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            // Authorization: `Bearer ${clientToken}`,
        },
        body: JSON.stringify(payload),
        };
        const result = await fetch(url, reqObj);
        const response = await result.json();
        return response;
    } catch (err) {
        console.log(err);
    }
    return null;
}