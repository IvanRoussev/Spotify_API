import axios from 'axios';
import { useEffect, useState } from 'react';

function App() {
  const [artist, setArtist] = useState([]);

  async function fetchData() {
    const response = await axios.get('/artist');
    setArtist(response.data);
  }

  useEffect(() => {
    fetchData();
  }, []);

  console.log(artist);

  // make a function that maps over the list of genres and return each item in list as a li element
  const genres = () => {
    return artist.list_genres.map((genre, index) => {
      return <li key={index}>{genre}</li>;
    });
  };

  console.log(genres);

  return (
    <div className='App'>
      <h1>{artist.name}</h1>
      <ul>Followers: {artist.followers}</ul>
      <ul>popularity rating: {artist.popularity_rating}</ul>
      <ul>Genres: {genres}</ul>
    </div>
  );
}

export default App;
