<template>
    <div id="naverIdLogin"></div>
</template>

<script type="text/javascript" src="https://static.nid.naver.com/js/naveridlogin_js_sdk_2.0.0.js" charset="utf-8"></script>
<script>
import { naverService } from '@/services/login/login';
export default {
    mounted() {
        naverService().setNaver();
    },
};
</script>