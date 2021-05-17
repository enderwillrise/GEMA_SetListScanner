import React from 'react';
import { StyleSheet, View, Image, Text, TouchableHighlight} from 'react-native';

function TakephotoScreen(props) {
    return (
        <View style={styles.container}>
       
      <View style={styles.header}>
          <Text style={styles.headerText}> New SetList</Text>
          <Image style= {styles.menuImage} source={require("../assets/kebab-menu.png")}></Image>
      </View>
       
       <View style={styles.block}>
       <TouchableHighlight onPress={()=> alert("SetList submitted")}>
       <View style={styles.submitButton}> 
            <Text style={styles.uploadsetlistText}> Submit </Text>
        </View>
        </TouchableHighlight>
        <TouchableHighlight onPress={()=> alert("Please retake the SetList")}>
        <View style={styles.retakeButton}> 
            <Text style={styles.uploadsetlistText}> Retake</Text>
        </View>
        </TouchableHighlight>

        

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

     submitButton: {
        top: 650,
        width: "50%",
        borderWidth: 7,
        paddingBottom: 20,
        paddingTop: 20,
        borderTopWidth: 7,
        borderColor: "lightgrey",
        

     }, 

     retakeButton: {
        
        left: 215,
        top: 560,
        width: "50%",
        borderWidth: 7,
        paddingBottom: 20,
        paddingTop: 20,
        borderTopWidth: 7,
        borderColor: "lightgrey",

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
       
        alignSelf: "center",
        fontWeight: "bold",
        fontSize: 30,
        color: "#cc0000",

     }

 })

export default TakephotoScreen;