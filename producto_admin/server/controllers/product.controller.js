const { Product } = require('../models/product.model');

// module.exports.index = (request, response) => {
//     response.json({
//         message: "Hello World"
//     });
// }
    // The method below is new
module.exports.createProduct = (req, res) => {
    console.log(req.body)
    const { title, price, description } = req.body;

    Product.create({
        title,
        price,
        description
    })
        .then(product => res.json(product))
        .catch(err => response.json(err))
}

module.exports.getAllProducts = (req, res) =>{
    Product.find()
        .then((products) => res.json({'products': products}))
        .catch(err => response.json(err))
}