check-env:
	@if [ ! -f swifty_api/server.env ]; then \
		echo "Erreur: Le fichier swifty_api/server.env est manquant"; \
		echo "Veuillez créer le fichier server.env avec les variables d'environnement nécessaires"; \
		exit 1; \
	elif [ ! -f swifty_companion_app/web/assets/flutter.env ]; then \
		echo "Erreur: Le fichier swifty_companion_app/web/assets/flutter.env est manquant"; \
		echo "Veuillez créer le fichier flutter.env avec les variables d'environnement nécessaires"; \
		exit 1; \
	fi
	@echo "Fichier d'environnement trouvé ✓"


install: check-env
	docker rmi -f swifty_server || true
	docker build -t swifty_server swifty_api
	cd swifty_companion_app && flutter pub get && cd ..


run: check-env
	docker stop swifty_server || true
	docker rm swifty_server || true
	docker run -d --env-file swifty_api/server.env --name swifty_server -p 5000:5000 swifty_server
	cd swifty_companion_app && flutter build web && flutter run -d web-server --web-port 8080

clean:
	docker stop swifty_server || true
	docker rm swifty_server || true
	docker rmi -f swifty_server || true
	rm -rf swifty_companion_app/web/build

all: install run

.PHONY: install run clean all check-env
