# HFT-OMS-EMS
Trade ordering & execution platform for a high frequency trading service.

## Goals:
1. Build driver to paper-trade & test high frequency algorithms.
1. Minor calculations about data, track products.
1. Set up p-queue for trade execution.
1. Customize data structures for low-latency-applications.

## Todos:
Implement file & class structure and pull into `driver.cpp` as main test application.

## Versions:
### 0.01
* `driver.cpp` - Main driver, can be used to run test suite
* `trade/` - All of OMS/EMS Classes
  * `order.cpp` - Holds classes for all securities & ordering
  * `execute.cpp` - TODO - class for managing fake PaperMoney portfolio and executing orders
