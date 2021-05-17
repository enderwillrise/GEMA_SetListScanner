import React from 'react';
import { StyleSheet, View, Image, Text} from 'react-native';

function HomeScreen(props) {
    return (
        <View style={styles.container}>
       <Image resizeMode= "contain" style={styles.logo} source={require("../assets/GEMA-logo.png")}></Image>
      <View style={styles.header}>
          <Text style={styles.headerText}>SetList</Text>
          <Image style= {styles.menuImage} source={require("../assets/kebab-menu.png")}></Image>
      </View>
       <View style={styles.block}>
       <View style={styles.newsetlistButton}> 
            <Text style={styles.newsetlistText}> New SetList </Text>
        </View>

        <View style={styles.mysetlistButton}> 
            <Text style={styles.newsetlistText}> My SetLists </Text>
        </View>

        <View style={styles.myprofileButton}> 
            <Text style={styles.newsetlistText}> My Profile </Text>
        </View>

        </View>
       </View>
    );
}

 const styles = StyleSheet.create({
    
    header: {
        backgroundColor: "#cc0000",
        flex: 0.18,

    },

    headerText: {
        color: "white",
        top:60,
        left: 30, 
        fontSize: 30,

    },
    
    menuImage: {
        width: 17,
        height: 25,
        top: 30,
        left: 390,

    },
    block: {
        
        alignSelf: "center",
        width: "100%",
        top: 50,

    },

    container: {
        flex: 1, 

    },

    logo: {
        height: 250,
        width: 250, 
      position: "absolute",
      top: 750,
      left: 230, 
    
     }, 

     newsetlistButton: {
        
        
        paddingBottom: 20,
        paddingTop: 20,
        borderTopWidth: 7,
        borderTopColor: "lightgrey",
        borderBottomWidth: 7, 
        borderBottomColor: "lightgrey",

     }, 

     mysetlistButton: {
        
        top: 40,
        paddingBottom: 20,
        paddingTop: 20,
        borderTopWidth: 7,
        borderTopColor: "lightgrey",
        borderBottomWidth: 7, 
        borderBottomColor: "lightgrey",

     }, 

     myprofileButton: {
        
        top: 80,
        paddingBottom: 20,
        paddingTop: 20,
        borderTopWidth: 7,
        borderTopColor: "lightgrey",
        borderBottomWidth: 7, 
        borderBottomColor: "lightgrey",

     }, 


     newsetlistText: {
        left: 20,
        alignSelf: "baseline",
        fontWeight: "bold",
        fontSize: 30,
        color: "#cc0000",

     }

 })

export default HomeScreen;