import {useState} from "react"
import axios from "axios"
import './App.css';

function App() {
  const [title, setTitle] = useState('')
  const [price, setPrice] = useState('')
  const [description, setDescription] = useState('')
  const [data, setData] = useState({})

  const handleSubmit = (e) => {
    e.preventDefault();
    const newProduct = {
      title: title,
      price: price,
      description: description
    }

    axios.post('http://localhost:8000/api/product/create', newProduct)
    .then(response => {
      setData(response.data)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  return (
    <div className="App">
      <h1>Add new product</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Title
        </label>
        <input type="text" value={title} onChange={(e) => setTitle(e.target.value)}/>
        <label>
          Price
        </label>
        <input type="number" value={price} onChange={(e) => setPrice(e.target.value)}/>
        <label>
          Description
        </label>
        <input type="text" value={description} onChange={(e) => setDescription(e.target.value)}/>
        <button>create</button>
      </form>
      {Object.keys(data).map((llave) => {
        return <p>{llave}: {data[llave]}</p>
      })}
    </div>
  );
}

export default App;
