import React, {useState, useEffect} from "react";
import axios from "axios";

function TopFiveArtist() {
  const [artists, setArtist] = useState([]);

  useEffect(async () => {
    const res = await axios.get("http://127.0.0.1:5000/top_artist");
    let {top5} = res.data;
    setArtist(top5);
  }, []);

  console.log("ARTISTS:", artists);

  return (
    <div>
      {typeof artists === "undefined"
        ? "Loading..."
        : artists.map((artist, i) => (
            <div key={i}>
              <img src={artist.image.url} alt={artist.name} />
              <p>{artist.name}</p>
            </div>
          ))}
    </div>
  );
}

export default TopFiveArtist;
