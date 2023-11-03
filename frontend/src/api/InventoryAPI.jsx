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

export const getProductById = (productId) => {
  return axios
    .get(`http://127.0.0.1:8000/inventory/products/${productId}/`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error(
        `There was an error fetching the product with ID ${productId}`,
        error
      );
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

export const getRoutesByCity = (cityName) => {
  return axios
    .get(
      `http://127.0.0.1:8000/delivery-to-shops/get-route-by-city/?city=${cityName}`
    )
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error fetching data", error);
    });
};

export const getRouteIDByCity = (cityName) => {
  return axios
    .get(
      `http://127.0.0.1:8000/delivery-to-shops/get-route-by-city/?city=${cityName}`
    )
    .then((response) => {
      if (response.data && response.data[0].RouteID) {
        return response.data[0].RouteID;
      } else {
        throw new Error(`No route found for city: ${cityName}`);
      }
    })
    .catch((error) => {
      console.error(
        `There was an error fetching RouteID for city ${cityName}`,
        error
      );
      throw error;
    });
};

export const addUser = (userData) => {
  return axios
    .post("http://127.0.0.1:8000/user/users/all/", userData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error adding the user", error);
      throw error;
    });
};

export const getUser = (userEmail) => {
  return axios
    .get(`http://127.0.0.1:8000/user/users/by_email/?email=${userEmail}`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error(
        `There was an error retrieving the user with email ${userEmail}`,
        error
      );
      throw error;
    });
};

export const addCustomer = (customerData) => {
  return axios
    .post("http://127.0.0.1:8000/customer/customers/all/", customerData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error adding the customer", error);
      throw error;
    });
};

export const addOrder = (orderData) => {
  return axios
    .post("http://127.0.0.1:8000/inventory/orders/", orderData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error adding the order", error);
    });
};

export const getOrdersByCustomer = (customerID) => {
  return axios
    .get(`http://127.0.0.1:8000/inventory/orders/customer/${customerID}/`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error retrieving the orders", error);
    });
};

export const addBill = (billData) => {
  return axios
    .post("http://127.0.0.1:8000/inventory/bills/", billData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error adding the bill", error);
      return Promise.reject(error);
    });
};

export const addBillEntry = (billEntryData) => {
  return axios
    .post("http://127.0.0.1:8000/inventory/bill-entries/", billEntryData)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error adding the bill entry", error);
    });
};

export const getBills = () => {
  return axios
    .get("http://127.0.0.1:8000/inventory/bills/")
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error retrieving the bills", error);
    });
};

export const getBillById = (billId) => {
  return axios
    .get(`http://127.0.0.1:8000/inventory/bills/${billId}/`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error(
        `There was an error retrieving the bill with ID ${billId}`,
        error
      );
    });
};

export const getStoreAndEndLocation = () => {
  return axios
    .get("http://127.0.0.1:8000/delivery-to-stores/get-store-and-end-location/")
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error(
        "There was an error fetching store and end location data",
        error
      );
      throw error;
    });
};
export const get_assigned_route_for_driver = (driverID) => {
  return axios
    .get(`http://127.0.0.1:8000/employee/driver-routes/${driverID}/`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error(
        "There was an error fetching the assigned route for the driver",
        error
      );
      throw error;
    });
};
export const getTopProducts = () => {
  return axios
    .get("http://127.0.0.1:8000/inventory/top-products/")
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error("There was an error fetching the top products", error);
      throw error;
    });
};

export const getSalesByCityAndRoute = () => {
  return axios
    .get("http://127.0.0.1:8000/inventory/sales-by-city-and-route/")
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error(
        "There was an error fetching sales by city and route",
        error
      );
      throw error;
    });
};
