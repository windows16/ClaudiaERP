# ClaudiaERP 🚀

Sistema de gestión empresarial con **Odoo 17** separado en módulos independientes: Inventario, Ventas y Compras.

## 📋 Requisitos

- **Docker** y **Docker Compose**
- **Git**

## 🚀 Instalación Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/windows16/ClaudiaERP.git
cd ClaudiaERP
```

## 2. levantar el proyecto 🐳 Con Docker (Recomendado)

### Opción más simple - Solo levantar el contenedor:

```bash
# En la raíz del proyecto
docker-compose up -d
```

**Espera 30-60 segundos** a que PostgreSQL y Odoo inicialicen.

Accede a: **http://localhost:8069**

**Credenciales iniciales:**
- **Email**: admin
- **Contraseña**: admin

### Ver logs:
```bash
docker-compose logs -f odoo
```

### Detener los contenedores:
```bash
docker-compose down
```

### Ver estado de contenedores:
```bash
docker-compose ps
```

## 🔧 Troubleshooting

### Contenedores no inician
```bash
docker-compose down -v
docker-compose up -d
```

### Módulos no aparecen
Accede a **Aplicaciones** y busca los módulos en el marketplace.

### Verificar que todo funciona
```bash
docker-compose ps
```

## 📦 Módulos

| Módulo | Descripción | Dependencias |
|--------|-------------|--------------|
| **inventario** | Gestión de productos, categorías y movimientos | base |
| **ventas** | Clientes y órdenes de venta | base, inventario |
| **compras** | Proveedores y órdenes de compra | base, inventario |

## ⚙️ Comandos Docker útiles

```bash
# Ver logs
docker-compose logs -f odoo

# Detener
docker-compose down

# Ver estado
docker-compose ps
```

1. **Configuración** → **Usuarios y Empresas** → **Grupos**
2. Crea grupos:
   - `Vendedores` - Acceso a Ventas
   - `Compradores` - Acceso a Compras
   - `Almacenistas` - Acceso a Inventario
   - `Gerentes` - Acceso a Reportes

3. Asigna usuarios a grupos según su rol


## 📂 Estructura del Proyecto

```
ClaudiaERP/
├── addons/
│   ├── inventario/        # Gestión de productos
│   ├── ventas/            # Gestión de ventas
│   └── compras/           # Gestión de compras
├── docker-compose.yml    # Para producción
└── README.md
```

## 📚 Documentación

- [Odoo Documentation](https://www.odoo.com/documentation/17.0/)

## 👨‍💻 Autor

Custom Development


