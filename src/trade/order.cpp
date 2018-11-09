#include <string>
#include <queue>
#include <vector>

/**
 * Create header file & import into driver
 */

using namespace std;
// base class for using queue
class Product {
private:
    string ticker;
    string item_id;
    float price;
    float low;
    float high;

    float high_3_month;
    float low_3_month;

    vector<Product> children;

    float mov_avg_30;
    float mov_avg_100;
    float file_close;
    float meu_close;
    float sigma_close;
    float delta_close;
    float vega_close;
    float theta_close;
    float gamma_close;
    float rho_close;
    
public:
    string getTickerSymbol() {
        return ticker;
    }
    void setTickerSymbol(string value) {
        // validation
        ticker = value;
    }

    string getItemId() {
        return item_id;
    }
    void setItemId(string value) {
        // validation
        item_id = value;
    }

    float getPrice() {
        return price;
    }
    void setPrice(float value) {
        price = value;
    }

    // Calculate greeks

    Product(string ticker, string item_id, float price) {
        setTickerSymbol(ticker);
        setItemId(item_id);
        setPrice(price);
    }
};

class Future : Product {

};

class Option : Product {

};

class ETF : Product {

};

class Commodity : Product {

};

class Stock : Product {

};

class Bond : Product {

};

class Forex : Product {

};

class Spread {

};

class BearSpread : Spread {

};

class BullSpread : Spread {

};

class CalendarSpread : Spread {

};


/**
 * Ordering System
 */
enum OrderType { BUY, SELL, LIMIT_BUY, LIMIT_SELL, STOP_LOSS, STOP_LIMIT };    // temporary, expand later
class Order {
private:
    OrderType order_type;
    Product prod;
    int quantity;
    float total_value;
public:
    OrderType getOrderType() {
        return order_type;
    }
    void setOrderType(OrderType value) {
        // validation
        order_type = value;
    }

    Product getProduct() {
        return prod;
    }
    void setProduct(Product p) {
        prod = p;
    }

    int getQuantity() {
        return quantity;
    }
    void setQuantity(int value) {
        quantity = value;
    }

    float getTotalValue() {
        return total_value;
    }
    void setTotalValue(float value) {
        total_value = value;
    }

    Order(OrderType order_type, Product& p, int quantity, float value) {
        setOrderType(order_type);
        setProduct(p);
        setQuantity(quantity);
        setTotalValue(value);
    }
};