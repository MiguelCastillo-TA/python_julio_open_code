const express = require("express");
const cors = require('cors')
const app = express();
const port = 8000;
require('./config/mongoose.config');

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true })); 

const AllProductRoutes = require('./routes/product.route');
AllProductRoutes(app)
    
// req es la abreviatura para request
// res es la abreviatura para response


app.listen( port, () => console.log(`Listening on port: ${port}`) );