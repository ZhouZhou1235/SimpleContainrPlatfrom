import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import { GArea } from './src/vars/ConstVar'

// https://vite.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vueDevTools(),
    ],
    resolve: {
        alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
        },
    },
    // vite 代理服务器
    server: {
        proxy: {
            '/api': {
                target: GArea.connectURL,
                changeOrigin: true,
                rewrite: (path)=>path.replace(/^\/api/,''),
            }
        }
    },
})
