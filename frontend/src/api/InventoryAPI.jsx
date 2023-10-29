import axios from "axios";

export const getProducts = () => {
  return axios
    .get("http://127.0.0.1:8000/inventory/products/")
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error fetching data", error);
    });
};

export const getProductsCount = () => {
  return axios
    .get("http://127.0.0.1:8000/inventory/products-count/")
    .then((response) => {
      return response.data.count;
    })
    .catch((error) => {
      console.error("There was an error fetching data", error);
    });
};

export const getCategories = () => {
  return axios
    .get("http://127.0.0.1:8000/inventory/categories/")
    .then((response) => {
      return response.data.categories;
    })
    .catch((error) => {
      console.error("There was an error fetching data", error);
    });
};

export const getRoutes = () => {
  return axios
    .get("http://127.0.0.1:8000/delivery-to-shops/truck-routes/")
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error fetching data", error);
    });
};

export const addUser = (userData) => {
  return axios
    .post("http://127.0.0.1:8000/user/users/", userData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error adding the user", error);
    });
};
