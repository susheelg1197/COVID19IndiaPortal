<template>
    <div>
        <nav-bar/>
        <div class="container section">
            <div class="columns">
                <div class="column is-8">
                    <slot/>
                </div>
                <div class="column is-4">
                    <side-bar/>
                </div>
            </div>
        </div>
        <footer-bar/>
    </div>
</template>
<script>
import Navbar from "@/components/Navbar"
import Sidebar from "@/components/Sidebar"
import footer from "@/components/footer"

export default {
    components:{
        Navbar,
        Sidebar,
        footer
    }
    
}
</script>