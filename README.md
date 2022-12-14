This project aims to solve the Rich Vehicle Routing Problem. 

The objective is to arrive at a problem as rich as the user indicates. Metaheuristic algorithms will be used to solve it, as well as leanrheuristic for those problems that are dynamic and symheuristic if the problem contains stochastic variables.

The following problems have been solved so far:
+ Static problems:
  - Vehicle Routing Problem (VRP): This is the most basic problem where there is no major restriction other than not exceeding the capacity of the truck, as well as not revisiting customers. Example:
  
  ![VRP](https://user-images.githubusercontent.com/82934982/194710612-204a0c9a-5698-4e92-9d80-0ed2d8275a75.png)
  - Arc Vehicle Routing Problem (AVRP): The basis of the problem is the VRP, however in this problem you have arcs. The arcs are directional, i.e., the distance between the same pair of nodes does not have to be the same. Example:
  
  ![AVRP](https://user-images.githubusercontent.com/82934982/194710620-48354a30-cf12-43f7-8cfd-74b7193a471b.png)
  - Multidepot Vehicle Routing Problem (MVRP): The basis of the problem is the VRP, however in this problem you have different depots from which different trucks can depart. Example:
  
  ![MVRP](https://user-images.githubusercontent.com/82934982/194710625-eb366255-bfeb-4fcd-8a99-280641129bc3.png)
- Time Windows Arc Vehicle Routing Problem (TWAVRP): The basis of the problem is the AVRP due to we need to take control of the order of deliveries. All customers have a time windows where trucks can delivery the good. If the truck arrives earlier it can wait but if it arrives late it can't serve the demand. Example:

![TWVRP](https://user-images.githubusercontent.com/82934982/195342778-3408c455-6230-4a8a-8f37-6bf47069a1ae.png)

- Time Windows Vehicle Routing Problem (TWVRP): The basis of the problem is the VRP due to we need to take control of the order of deliveries. All customers have a time windows where trucks can delivery the good. If the truck arrives earlier it can wait but if it arrives late it can't serve the demand. Example:

![TWVRP2](https://user-images.githubusercontent.com/82934982/197335207-69471925-3355-4d24-a4fb-cdd4dbca034b.png)

+ Stochastic problems:
  - SVRP: This is the most basic problem where there is no major restriction other than not exceeding the capacity of the truck, as well as not revisiting customers. Analysis example:
  
  ![SVRP](https://user-images.githubusercontent.com/82934982/194710643-2d6cfcc4-c7ef-410b-88fc-ba553ed33be0.png) 
  
  - Stochastic Multidepot Vehicle Routing Problem (SMVRP):     .Analysis example:
  
  ![SMVRP](https://user-images.githubusercontent.com/82934982/194710649-845c2313-e7b8-461e-91cc-d6802b0ff12c.png)

Linkedin pages:
  - Juan Francisco G??mez: www.linkedin.com/in/juan-francisco-g??mez-gonz??lez-04110a175
