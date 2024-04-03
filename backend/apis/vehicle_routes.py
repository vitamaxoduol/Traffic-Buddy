from flask import jsonify, request
from models.vehicle import Vehicle
from models.dbconfig import db
from authentication import authenticate_api


def vehicles_apis(app, db):
    @app.route("/api/vehicles", methods=["GET"])
    @authenticate_api
    def get_vehicles():
        vehicles = Vehicle.query.all()
        vehicle_list = [{"id": vehicle.id, "license_plate": vehicle.license_plate, "make": vehicle.make, "model": vehicle.model, "color": vehicle.color} for vehicle in vehicles]
        return jsonify({"vehicles": vehicle_list}), 200

    # Route to retrieve details of a specific vehicle
    @app.route("/api/vehicles/<int:vehicle_id>", methods=["GET"])
    @authenticate_api
    def get_vehicle(vehicle_id):
        vehicle = Vehicle.query.get(vehicle_id)
        if vehicle:
            return jsonify({"id": vehicle.id, "license_plate": vehicle.license_plate, "make": vehicle.make, "model": vehicle.model, "color": vehicle.color}), 200
        else:
            return jsonify({"error": "Vehicle not found"}), 404

    # Route to create a new vehicle
    @app.route("/api/vehicles", methods=["POST"])
    @authenticate_api
    def create_vehicle():
        data = request.get_json()
        if not data or "license_plate" not in data or "make" not in data or "model" not in data or "color" not in data:
            return jsonify({"error": "Invalid or missing vehicle data"}), 400
        
        # Create a new vehicle
        vehicle = Vehicle(
            license_plate=data["license_plate"],
            make=data["make"],
            model=data["model"],
            color=data["color"],
            owner_name=data.get("owner_name"),
            user_id=data.get("user_id")
        )
        db.session.add(vehicle)
        db.session.commit()

        return jsonify({"message": "Vehicle created successfully", "vehicle_id": vehicle.id}), 201

    # Route to update details of a specific vehicle
    @app.route("/api/vehicles/<int:vehicle_id>", methods=["PUT"])
    @authenticate_api
    def update_vehicle(vehicle_id):
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return jsonify({"error": "Vehicle not found"}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided for update"}), 400

        # Update vehicle details
        if "license_plate" in data:
            vehicle.license_plate = data["license_plate"]
        if "make" in data:
            vehicle.make = data["make"]
        if "model" in data:
            vehicle.model = data["model"]
        if "color" in data:
            vehicle.color = data["color"]
        if "owner_name" in data:
            vehicle.owner_name = data["owner_name"]
        if "user_id" in data:
            vehicle.user_id = data["user_id"]

        db.session.commit()
        return jsonify({"message": "Vehicle updated successfully"}), 200

    # Route to delete a specific vehicle
    @app.route("/api/vehicles/<int:vehicle_id>", methods=["DELETE"])
    @authenticate_api
    def delete_vehicle(vehicle_id):
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return jsonify({"error": "Vehicle not found"}), 404

        db.session.delete(vehicle)
        db.session.commit()
        return jsonify({"message": "Vehicle deleted successfully"}), 200