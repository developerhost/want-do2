<template>
  <v-app>
    <!-- <v-app-bar
      app
      color="primary"
      dark
    >
     

      
    </v-app-bar> -->
    <div></div>
    <v-container>
      <v-row>
        <v-col></v-col>
      </v-row>
    </v-container>


    <div id="nav">
      <router-link to="/about">About</router-link>
      <router-link to="/signup">Signup</router-link>
      <router-link to="/">task</router-link>

    </div>
    <router-view/>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    // HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
