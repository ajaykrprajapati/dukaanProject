# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# import logging

# logger = logging.getLogger("django.server")


# class BaseView(APIView):
#     def data_response(self, message, data):
#         return Response(
#             {"result": True, "message": message, "data": data},
#             status=status.HTTP_200_OK,
#         )

#     def resource_created_response(self, resource, resource_id):
#         return Response(
#             {
#                 "result": True,
#                 "message": f"{resource} created successfully",
#                 "id": resource_id,
#             },
#             status=status.HTTP_201_CREATED,
#         )

#     def resource_updated_response(self, resource, resource_id):
#         return Response(
#             {
#                 "result": True,
#                 "message": f"{resource} with {resource_id} updated successfully",
#             },
#             status=status.HTTP_202_ACCEPTED,
#         )

#     def resource_deleted_response(self, message, resource_id=None):
#         return Response(
#             {"result": True, "message": message},
#             status=status.HTTP_202_ACCEPTED,
#         )

#     def serializer_error_response(self, message, serializer_errors):
#         serializer_errors = " ".join(
#             [
#                 error_key + " : " + error_detail[0]
#                 for error_key, error_detail in serializer_errors.items()
#             ]
#         )
#         return self.bad_request_response(message + " " + serializer_errors)

#     def bad_request_response(self, message):
#         # Handles Error Objects Internally by Converting them To String
#         return Response(
#             {"result": False, "message": str(message)},
#             status=status.HTTP_400_BAD_REQUEST,
#         )

#     def resource_not_found_response(self, resource, id=None):
#         return Response(
#             {
#                 "result": False,
#                 "message": f"Resource {resource} with Id {id} doesn't exist ",
#             },
#             status=status.HTTP_404_NOT_FOUND,
#         )

#     def org_doesnot_exist_response(self, org_id):
#         return self.resource_not_found_response("Organization", org_id)

#     def unauthorized_response(self, message="Unauthorized Access"):
#         return Response(
#             {"result": False, "message": message},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )

#     def upload_file_response(self, file_url):
#         return Response(
#             {
#                 "result": True,
#                 "message": "Media created successfully",
#                 "media-url": file_url,
#             }
#         )

#     class Meta:
#         abstract = True
