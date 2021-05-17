import React from 'react';
import { View, StyleSheet, Text, Image} from 'react-native';


function WelcomeScreen(props) {
 return (
    <View style = {styles.background}>
        
        
        <View style={styles.loginButton}> 
            <Text style={styles.basedText}> Sign Up </Text>
        </View>
        
        <View style={styles.registerButton}>
            <Text style={styles.loginText}> Login </Text>
         </View>

        <View style={styles.container}>
          <Image style={styles.logo} source={require("../assets/GEMA-logo.png")}/>
          <Text style={styles.gemaText}>GEMA</Text>
          <Text style={styles.setlistText}>SetList</Text>
        </View>
         

    </View>
    );
}
const styles = StyleSheet.create({
   backgroundColor: {
        flex: 1, 
        justifyContent: "flex-end",
        alignItems: "center",

   },
  
    gemaText: {
         
        
        top: 50,
        right: 50,
        fontSize: 60,
        fontWeight: "bold",
        color: "black",
       

    },

    setlistText: {
         
        top: 60,
        right: 55,
        fontSize: 60,
        fontWeight: "bold",
        color: "#cc0000",
       

    },


    container: {
        position: "absolute",
        
        top:150,
        left: 180,
    },

    loginButton: {
        
        top: 715,
        
        alignSelf: "center",
        width: "80%",
        height: 70,
        backgroundColor: "#cc0000",
        
    }, 

    registerButton: {
        top: 730,
        
        alignSelf: "center",
        width: "80%",
        height: 70,
        borderWidth: 2, 
        borderColor: "#cc0000",
       

    }, 

    basedText: {
        alignSelf: "center",
        top: 17,
        fontSize: 30,
        color: "white",
    },

    loginText: {
        alignSelf: "center",
        top: 17,
        fontSize: 30,
        color: "#cc0000",
    }

    
})
export default WelcomeScreen;