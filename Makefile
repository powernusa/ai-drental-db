# ------------------------------------------------------
# AI Rental DB — Makefile Automation Commands
# ------------------------------------------------------

# Run docker compose with rebuild
up:
	@echo "🚀 Starting containers with rebuild..."
	docker compose up --build

# Start containers without rebuild (faster)
start:
	@echo "🚀 Starting containers..."
	docker compose up

# Stop containers (keep volumes)
stop:
	@echo "🛑 Stopping containers..."
	docker compose down

# Stop and remove containers + volumes (wipe DB)
reset:
	@echo "🔥 Resetting stack (containers + volumes)..."
	docker compose down -v
	@echo "💥 All volumes removed. Rebuilding..."
	docker compose up --build

# Enter analytics container
analytics-shell:
	@echo "🔍 Entering analytics container..."
	docker exec -it drental-analytics bash

# Enter postgres container
db-shell:
	@echo "📦 Entering PostgreSQL container..."
	docker exec -it drental-docker bash

# List running containers
ps:
	@echo "📋 Listing running containers..."
	docker ps

# Remove orphaned containers/images (cleanup)
prune:
	@echo "🧹 Cleaning unused Docker objects..."
	docker system prune -f

# Show logs from postgres
logs-db:
	@echo "📜 PostgreSQL logs:"
	docker logs drental-docker

# Show logs from analytics
logs-analytics:
	@echo "📜 Analytics logs:"
	docker logs drental-analytics
