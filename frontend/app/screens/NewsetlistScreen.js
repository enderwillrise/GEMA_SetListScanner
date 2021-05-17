import React from 'react';
import { StyleSheet, View, Image, Text} from 'react-native';

function NewsetlistScreen(props) {
    return (
        <View style={styles.container}>
       <Image resizeMode= "contain" style={styles.logo} source={require("../assets/GEMA-logo.png")}></Image>
      <View style={styles.header}>
          <Text style={styles.headerText}> New SetList</Text>
          <Image style= {styles.menuImage} source={require("../assets/kebab-menu.png")}></Image>
      </View>
       <View style={styles.block}>
       <View style={styles.uploadsetlistButton}> 
            <Text style={styles.uploadsetlistText}> Upload SetList </Text>
        </View>

        <View style={styles.takephotoButton}> 
            <Text style={styles.uploadsetlistText}> Take Phote </Text>
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

     uploadsetlistButton: {
        
        
        paddingBottom: 20,
        paddingTop: 20,
        borderTopWidth: 7,
        borderTopColor: "lightgrey",
        borderBottomWidth: 7, 
        borderBottomColor: "lightgrey",

     }, 

     takephotoButton: {
        
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


     uploadsetlistText: {
        left: 20,
        alignSelf: "baseline",
        fontWeight: "bold",
        fontSize: 30,
        color: "#cc0000",

     }

 })

export default NewsetlistScreen;