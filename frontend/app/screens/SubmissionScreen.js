import React from 'react';
import { StyleSheet, View, Image, Text} from 'react-native';

function SubmissionScreen(props) {
    return (
        <View style={styles.container}>
       
      <View style={styles.header}>
          <Text style={styles.headerText}> New SetList</Text>
          <Image style= {styles.menuImage} source={require("../assets/kebab-menu.png")}></Image>
      </View>
       <View style={styles.block}>
       <Text style={styles.submissionText}>
           Your submisson has been processed. {"\n"}{"\n"}
           Please check your email for a confirmation. 
       </Text>
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

    submissionText: {
        top: 100,
        paddingRight: 20,
        paddingLeft: 20,
        textAlign: "center",
        color: "#cc0000",
        fontWeight: "bold",
        fontSize: 30,

    },

    container: {
        flex: 1, 

    }

    


     

     



     

 })

export default SubmissionScreen;