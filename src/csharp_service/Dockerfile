FROM mcr.microsoft.com/dotnet/sdk:6.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY CsharpService.csproj CsharpService.csproj
RUN dotnet restore CsharpService.csproj
COPY . .
WORKDIR /src
RUN dotnet build CsharpService.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish -c Release -p:PublishReadyToRun=true --self-contained=true -r linux-x64 -o /app

FROM ubuntu:22.04 AS final

RUN apt update && apt install -qqq libicu70

COPY --from=publish /app /opt/CsharpService
WORKDIR /opt/CsharpService

CMD [ "/opt/CsharpService/CsharpService" ]
