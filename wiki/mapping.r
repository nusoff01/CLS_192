library(ggmap)
library(maptools)
library(maps)


myLocation <- c(-170, -50, 170, 70)


myMap <- get_map(location=myLocation, source="stamen", maptype="watercolor", zoom=3,color="bw", crop=FALSE)

locations2 <- read.csv("~/GitHub/nusoff01/CLS_192/CLS_192/wiki/locations/blues_rock.csv")
locations1 <- read.csv("~/GitHub/nusoff01/CLS_192/CLS_192/wiki/locations/industrial_present.csv")

d1 <- data.frame(lat=c(50, 50, 50),
                lon=c(0, 10, 20), 
                area=c(.5,.4,.5))

d2 <- data.frame(lat=c(20, 20, 20),
                 lon=c(0, 10, 20), 
                 area=c(1,4,5))


ggmap(myMap) + geom_point(data=locations1, aes(x=Long, y=Lat, size=num),color="blue", alpha=.6)+ 
               # geom_point(data=locations2, aes(x=Long, y=Lat, size=num), color="red", alpha=.6)+
               scale_size(range=c(3,6)) + labs(title="industrial, present")
